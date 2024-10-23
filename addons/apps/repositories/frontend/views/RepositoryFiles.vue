<template>
    <v-container fluid class="pa-0">

        <!-- Repository header -->
        <v-row v-if="repo.id" no-gutters class="px-4 py-2 align-center">
            <v-col cols="auto">
                <div class="d-flex align-center">
                    <div>
                        <v-select v-model="selectedProject" :items="projects" item-text="name" item-value="id"
                            label="Repository" @change="loadRepository" hide-details dense></v-select>
                    </div>
                    <!-- Add a create repository button -->
                    <v-btn
                        v-if="!repo.id"
                        small
                        color="primary"
                        class="ml-2"
                        @click="openCreateRepoDrawer"
                    >
                        <v-icon left small>mdi-plus</v-icon>
                        Create Repo
                    </v-btn>
                    <div class="ml-2">
                        <v-icon left>mdi-source-repository</v-icon>
                        <span class="font-weight-bold">{{ repoOwner }} / {{ repoName }}</span>
                        <v-chip x-small label class="ml-2">{{ repoVisibility }}</v-chip>
                        <!-- Refreshing the page -->
                        <v-btn icon @click="defaultFetch">
                            <v-icon>mdi-refresh</v-icon>
                        </v-btn>
                    </div>
                </div>
            </v-col>
            <v-spacer></v-spacer>
            <v-col cols="auto">
                <v-btn small text class="mr-2" disabled>
                    <v-icon left small>mdi-rss</v-icon>
                    Watch
                    <v-chip x-small class="ml-1">{{ watchCount }}</v-chip>
                </v-btn>
                <v-btn small text class="mr-2" disabled>
                    <v-icon left small>mdi-star-outline</v-icon>
                    Star
                    <v-chip x-small class="ml-1">{{ starCount }}</v-chip>
                </v-btn>
                <v-btn small text disabled>
                    <v-icon left small>mdi-source-fork</v-icon>
                    Fork
                    <v-chip x-small class="ml-1">{{ forkCount }}</v-chip>
                </v-btn>
            </v-col>
        </v-row>

        <!-- No Repository Card -->
        <v-card v-if="!repo.id" class="mx-auto my-12" max-width="400">
            <v-img
                class="white--text align-end"
                height="200px"
                src="/path/to/repository-image.jpg"
            >
                <v-card-title>No Repository Found</v-card-title>
            </v-img>

            <v-card-subtitle class="pb-0">
                It looks like there's no repository here yet.
            </v-card-subtitle>

            <v-card-text class="text--primary">
                <div>Create a new repository to get started with your project.</div>
                <div>You can store your code, track changes, and collaborate with others.</div>
            </v-card-text>

            <v-card-actions>
                <v-btn
                    color="primary"
                    text
                    @click="openCreateRepoDrawer"
                >
                    Create Repository
                </v-btn>
                <v-btn
                    color="secondary"
                    text
                    @click="showRepositoryTutorial"
                >
                    Learn More
                </v-btn>
            </v-card-actions>
        </v-card>

        <!-- Existing Repository Content -->
        <template v-else>
            <!-- Navigation tabs -->
            <v-tabs elevation="0">
                <v-tab>
                    <v-icon left>mdi-code-tags</v-icon>
                    Code
                </v-tab>
                <!-- <v-tab>
            <v-icon left>mdi-alert-circle-outline</v-icon>
            Issues
          </v-tab>
          <v-tab>
            <v-icon left>mdi-source-pull</v-icon>
            Pull Requests
          </v-tab>
          <v-tab>
            <v-icon left>mdi-play-circle-outline</v-icon>
            Actions
          </v-tab>
          <v-tab>
            <v-icon left>mdi-package-variant-closed</v-icon>
            Packages
          </v-tab>
          <v-tab>
            <v-icon left>mdi-view-grid-outline</v-icon>
            Projects
          </v-tab>
          <v-tab>
            <v-icon left>mdi-tag-outline</v-icon>
            Releases
          </v-tab>
          <v-tab>
            <v-icon left>mdi-book-open-page-variant</v-icon>
            Wiki
          </v-tab>
          <v-tab>
            <v-icon left>mdi-chart-line</v-icon>
            Activity
          </v-tab> -->
                <v-spacer></v-spacer>
                <v-btn icon class="align-self-center mr-4">
                    <v-icon>mdi-cog</v-icon>
                </v-btn>
            </v-tabs>

            <!-- Repository info -->
            <v-card flat class="pa-4">
                <div class="text-subtitle-2 mb-2">{{ repoDescription }}</div>
                <v-row no-gutters>
                    <v-col cols="3">
                        <v-icon small class="mr-1">mdi-source-commit</v-icon>
                        <span class="text-caption">{{ commitCount }} Commits</span>
                    </v-col>
                    <v-col cols="3">
                        <v-icon small class="mr-1">mdi-source-branch</v-icon>
                        <span class="text-caption">{{ branchCount }} Branches</span>
                    </v-col>
                    <v-col cols="3">
                        <v-icon small class="mr-1">mdi-tag</v-icon>
                        <span class="text-caption">{{ tagCount }} Tags</span>
                    </v-col>
                    <v-col cols="3" class="text-right">
                        <span class="text-caption">{{ repoSize }}</span>
                    </v-col>
                </v-row>
            </v-card>

            <!-- File explorer -->
            <v-card flat class="pa-4">
                <v-row no-gutters align="center" class="mb-4">
                    <v-col cols="auto">
                        <v-select v-model="selectedBranch" :items="branches" label="Branch" dense outlined hide-details
                            class="branch-select"></v-select>
                    </v-col>
                    <!-- <v-col cols="auto" class="ml-4">
                        <v-btn small outlined>Go to file</v-btn>
                    </v-col>
                    <v-col cols="auto" class="ml-2">
                        <v-btn small outlined>Add file<v-icon right>mdi-menu-down</v-icon></v-btn>
                    </v-col> -->
                    <v-spacer></v-spacer>
                    <v-col cols="auto">
                        <v-btn-toggle v-model="cloneMethod" mandatory>
                            <v-btn small value="clone_url">HTTPS</v-btn>
                            <v-btn small value="ssh_url">SSH</v-btn>
                        </v-btn-toggle>
                    </v-col>
                    <v-col cols="auto" class="ml-2">
                        <v-text-field :value="cloneMethod == 'clone_url' ? repo.clone_url : repo.ssh_url"
                            append-icon="mdi-content-copy" readonly dense outlined hide-details></v-text-field>
                    </v-col>
                    <v-col cols="auto" class="ml-2">
                        <v-btn icon><v-icon>mdi-dots-horizontal</v-icon></v-btn>
                    </v-col>
                </v-row>

                <v-skeleton-loader
                    v-if="isLoadingFiles"
                    type="table"
                ></v-skeleton-loader>
                <v-simple-table v-else>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left">Name</th>
                                <th class="text-left">Last commit</th>
                                <th class="text-left">Commit time</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="file in files" :key="file.name">
                                <td>
                                    <v-icon left small>mdi-file-document-outline</v-icon>
                                    {{ file.name }}
                                </td>
                                <td>{{ file.last_commit_message }}</td>
                                <td>{{ file.last_commit_time }}</td>
                            </tr>
                            <!-- <tr>
                                <td>
                                    <v-icon left small>mdi-file-document-outline</v-icon>
                                    README.md
                                </td>
                                <td>Initial commit</td>
                                <td>14 hours ago</td>
                            </tr> -->
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>

            <!-- README preview -->
            <!-- <v-card flat class="pa-4 mt-4">
                <div class="d-flex align-center mb-4">
                    <h2 class="text-h5">{{ readmeContent.name }}</h2>
                    <v-spacer></v-spacer>
                    <v-btn icon><v-icon>mdi-pencil</v-icon></v-btn>
                </div>
                <v-card outlined>
                    <v-card-text>
                        {{ readmeContent }}
                    </v-card-text>
                </v-card>
            </v-card> -->
        </template>

        <!-- Add a loader overlay -->
        <v-overlay :value="isLoading" absolute>
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
    </v-container>
</template>

<script>
import { bus } from '@/main'

export default {
    props: {
        pid: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            selectedProject: null,
            repo: {},
            projects: [],
            repoOwner: '',
            repoName: '',
            repoVisibility: '',
            repoDescription: '',
            watchCount: 0,
            starCount: 0,
            forkCount: 0,
            commitCount: 0,
            branchCount: 0,
            tagCount: 0,
            repoSize: '',
            selectedBranch: '',
            branches: [],
            cloneMethod: 0,
            files: [],
            readmeContent: '',
            isLoading: false,
            isLoadingFiles: false,
        };
    },
    async created() {
        await this.defaultFetch();
        bus.$on('form_success', (response, form_name, form_type = null) => {
            console.log(response, form_name, form_type)
            this.$store.dispatch('CloseDrawer')

            this.fetchProjects()
        })
    },
    methods: {
        async defaultFetch() {
            this.isLoading = true;
            try {
                await this.fetchProjects();
                // await this.fetchRepositoryData();
                // await this.fetchBranches();
                // await this.fetchContents();
                // await this.fetchCommits();
            } finally {
                this.isLoading = false;
            }
        },
        async fetchProjects() {
            this.isLoading = true;
            try {
                const response = await this.$store.dispatch('RepositoriesStore/GET_repositories', `?project=${this.pid ? this.pid : ''}`);
                this.projects = response.data.results;
                if (this.projects.length > 0) {
                    this.selectedProject = this.projects[0].id;
                    await this.loadRepository();
                }
            } catch (error) {
                console.error('Error fetching projects:', error);
            } finally {
                this.isLoading = false;
            }
        },
        async loadRepository() {
            this.isLoading = true;
            try {
                if (this.selectedProject) {
                    await this.fetchRepositoryData();
                    if (this.repo.id) {
                        await this.fetchBranches();
                        await this.fetchCommits();
                        await this.fetchContents();
                    }
                }
            } finally {
                this.isLoading = false;
            }
        },
        async fetchCommits() {
            this.isLoading = true;
            try {
                const response = await this.$store.dispatch('RepositoriesStore/GET_repositories',`${this.selectedProject}/commits/`);
                this.commits = response.data;
                this.commitCount = this.commits.length;
            } finally {
                this.isLoading = false;
            }
        },
        async fetchRepositoryData() {
            this.isLoading = true;
            try {
                const response = await this.$store.dispatch('RepositoriesStore/GET_repositories',`${this.selectedProject}/details/`);
                const repo = response.data.repository;
                this.repo = repo;
                this.repoOwner = repo.owner.login;
                this.repoName = repo.name;
                this.repoVisibility = repo.private ? 'Private' : 'Public';
                this.repoDescription = repo.description;
                this.watchCount = repo.watchers_count;
                this.starCount = repo.stars_count;
                this.forkCount = repo.forks_count;
                // Note: Some properties might not be available directly, you may need to make additional API calls
                this.commitCount = repo.default_branch_commit_count || 0;
                this.tagCount = repo.release_counter || 0;
                this.repoSize = `${(repo.size / 1024).toFixed(2)} KiB`;
            } catch (error) {
                console.error('Error fetching repository data:', error);
            } finally {
                this.isLoading = false;
            }
        },
        async fetchBranches() {
            this.isLoading = true;
            try {
                const response = await this.$store.dispatch('RepositoriesStore/GET_repositories',`${this.selectedProject}/branches/`);
                this.branches = response.data.map(branch => branch.name);
                this.branchCount = this.branches.length;
                this.selectedBranch = this.branches[0] || '';
            } catch (error) {
                console.error('Error fetching branches:', error);
            } finally {
                this.isLoading = false;
            }
        },
        async fetchContents() {
            this.isLoadingFiles = true;
            try {
                const response = await this.$store.dispatch('RepositoriesStore/GET_repositories', `${this.selectedProject}/contents/?ref=${this.selectedBranch}`);
                const files = response.data.filter(item => item.type === 'file');

                // Fetch commit information for each file
                const filesWithCommits = await Promise.all(files.map(async (file) => {
                    const commitResponse = await this.$store.dispatch('RepositoriesStore/GET_repositories', `${this.selectedProject}/commits/?path=${file.path}&per_page=1`);
                    const lastCommit = commitResponse.data[0];
                    return {
                        ...file,
                        last_commit_message: lastCommit ? lastCommit.commit.message : '',
                        last_commit_time: lastCommit ? new Date(lastCommit.commit.author.date).toLocaleString() : '',
                    };
                }));

                this.files = filesWithCommits;

                const readme = this.files.find(item => item.name.toLowerCase() === 'readme.md');
                if (readme) {
                    const readmeResponse = await this.$store.dispatch(readme.download_url);
                    this.readmeContent = readmeResponse.data;
                }
            } catch (error) {
                console.error('Error fetching contents:', error);
            } finally {
                this.isLoadingFiles = false;
            }
        },
        openCreateRepoDrawer() {
            console.log('openCreateRepoDrawer');
            this.$store.dispatch('OpenDrawerOnClick', {
                ShowAppBarOnDrawer: true,
                DrawerSize: '30%',
                DrawerFormType: 'repo_form',
                DrawerFormTitle: 'Create Repo',
                DrawerAddons: '/addons/apps/repositories/api/repositories',
                DrawerFormAPICall: true,
                DrawerFilterForm: false,
                DrawerMutation: 'mutation__drawer',
                DrawerExtraParam: `&project=${this.pid ? this.pid: ''}`,
                DrawerActionType: 'new',
                DrawerFormSubmit: {
                    btn_name: 'Create Repo',
                    store_action_name: 'RepositoriesStore/CREATE_repositories',
                    custom_action: '',
                    data: '',
                },
            });
        },
        showRepositoryTutorial() {
            // Implement a method to show a tutorial or documentation about repositories
            console.log('Show repository tutorial');
        },
    },
};
</script>
<style scoped>
.branch-select {
    max-width: 150px;
}
</style>


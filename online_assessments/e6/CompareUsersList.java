import java.io.*;
import java.util.*;
import java.time.LocalDate;

class User {
    private int id;
    private String identityNumber;
    private String firstName;
    private String lastName;
    private int age;
    private LocalDate birthDate;
    private String email;
    private String gender;
    private String country;
    private String city;
    private String address;
    private String zipCode;
    private String phoneNumber;
    private String department;
    private String roles;
    private LocalDate joinDate;
    private double credit;
    private String status;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getIdentityNumber() {
        return identityNumber;
    }

    public void setIdentityNumber(String identityNumber) {
        this.identityNumber = identityNumber;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public LocalDate getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getZipCode() {
        return zipCode;
    }

    public void setZipCode(String zipCode) {
        this.zipCode = zipCode;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getRoles() {
        return roles;
    }

    public void setRoles(String roles) {
        this.roles = roles;
    }

    public LocalDate getJoinDate() {
        return joinDate;
    }

    public void setJoinDate(LocalDate joinDate) {
        this.joinDate = joinDate;
    }

    public double getCredit() {
        return credit;
    }

    public void setCredit(double credit) {
        this.credit = credit;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}

class UserManager {
    /*
     * Complete the 'compareUsers' function below.
     * The function is expected to return two lists which are updated and inserted.
     * The function accepts two lists:
     *  - usersListInDB
     *  - newUsersList
     */
    @SuppressWarnings("unchecked")
    public static List<User>[] compareUsers(List<User> usersListInDB, List<User> newUsersList) {
        // Prepare result lists
        List<User> updatedUsers = new ArrayList<>();
        List<User> insertedUsers = new ArrayList<>();

        // Create a map of current DB users for quick lookup
        Map<Integer, User> dbMap = new HashMap<>();
        for (User dbUser : usersListInDB) {
            dbMap.put(dbUser.getId(), dbUser);
        }

        // Iterate over newUsersList
        for (User newUser : newUsersList) {
            // Check if it's a new user
            if (newUser.getId() == 0) {
                insertedUsers.add(newUser);
            } else {
                // If it has a valid ID, compare with DB record
                User dbUser = dbMap.get(newUser.getId());
                if (dbUser != null) {
                    // Inline comparison
                    boolean isDifferent = false;
                    if (!Objects.equals(dbUser.getIdentityNumber(), newUser.getIdentityNumber())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getFirstName(), newUser.getFirstName())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getLastName(), newUser.getLastName())) isDifferent = true;
                    else if (dbUser.getAge() != newUser.getAge()) isDifferent = true;
                    else if (!Objects.equals(dbUser.getBirthDate(), newUser.getBirthDate())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getEmail(), newUser.getEmail())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getGender(), newUser.getGender())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getCountry(), newUser.getCountry())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getCity(), newUser.getCity())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getAddress(), newUser.getAddress())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getZipCode(), newUser.getZipCode())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getPhoneNumber(), newUser.getPhoneNumber())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getDepartment(), newUser.getDepartment())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getRoles(), newUser.getRoles())) isDifferent = true;
                    else if (!Objects.equals(dbUser.getJoinDate(), newUser.getJoinDate())) isDifferent = true;
                    else if (Double.compare(dbUser.getCredit(), newUser.getCredit()) != 0) isDifferent = true;
                    else if (!Objects.equals(dbUser.getStatus(), newUser.getStatus())) isDifferent = true;

                    if (isDifferent) {
                        updatedUsers.add(newUser);
                    }
                }
            }
        }

        return new List[]{updatedUsers, insertedUsers};
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.getenv("OUTPUT_PATH"), "UTF-8");

        List<User> usersListInDB = new ArrayList<>();
        List<User> newUsersList = new ArrayList<>();

        int userInDbCount = Integer.parseInt(reader.readLine().trim());
        for (int i = 0; i < userInDbCount; i++) {
            String[] u = reader.readLine().trim().split(",");
            User usr = new User();
            usr.setId(u[0].isEmpty() ? 0 : Integer.parseInt(u[0]));
            usr.setIdentityNumber(u[1]);
            usr.setFirstName(u[2]);
            usr.setLastName(u[3]);
            usr.setAge(u[4].isEmpty() ? 0 : Integer.parseInt(u[4]));
            usr.setBirthDate(u[5].isEmpty() ? null : LocalDate.of(
                    Integer.parseInt(u[5].split("\\.")[0]),
                    Integer.parseInt(u[5].split("\\.")[1]),
                    Integer.parseInt(u[5].split("\\.")[2])
            ));
            usr.setEmail(u[6]);
            usr.setGender(u[7]);
            usr.setCountry(u[8]);
            usr.setCity(u[9]);
            usr.setAddress(u[10]);
            usr.setZipCode(u[11]);
            usr.setPhoneNumber(u[12]);
            usr.setDepartment(u[13]);
            usr.setRoles(u[14]);
            usr.setJoinDate(u[15].isEmpty() ? null : LocalDate.of(
                    Integer.parseInt(u[15].split("\\.")[0]),
                    Integer.parseInt(u[15].split("\\.")[1]),
                    Integer.parseInt(u[15].split("\\.")[2])
            ));
            usr.setCredit(u[16].isEmpty() ? 0.0 : Double.parseDouble(u[16]));
            usr.setStatus(u[17]);
            usersListInDB.add(usr);
        }

        int newUsersCount = Integer.parseInt(reader.readLine().trim());
        for (int i = 0; i < newUsersCount; i++) {
            String[] u = reader.readLine().trim().split(",");
            User usr = new User();
            usr.setId(u[0].isEmpty() ? 0 : Integer.parseInt(u[0]));
            usr.setIdentityNumber(u[1]);
            usr.setFirstName(u[2]);
            usr.setLastName(u[3]);
            usr.setAge(u[4].isEmpty() ? 0 : Integer.parseInt(u[4]));
            usr.setBirthDate(u[5].isEmpty() ? null : LocalDate.of(
                    Integer.parseInt(u[5].split("\\.")[0]),
                    Integer.parseInt(u[5].split("\\.")[1]),
                    Integer.parseInt(u[5].split("\\.")[2])
            ));
            usr.setEmail(u[6]);
            usr.setGender(u[7]);
            usr.setCountry(u[8]);
            usr.setCity(u[9]);
            usr.setAddress(u[10]);
            usr.setZipCode(u[11]);
            usr.setPhoneNumber(u[12]);
            usr.setDepartment(u[13]);
            usr.setRoles(u[14]);
            usr.setJoinDate(u[15].isEmpty() ? null : LocalDate.of(
                    Integer.parseInt(u[15].split("\\.")[0]),
                    Integer.parseInt(u[15].split("\\.")[1]),
                    Integer.parseInt(u[15].split("\\.")[2])
            ));
            usr.setCredit(u[16].isEmpty() ? 0.0 : Double.parseDouble(u[16]));
            usr.setStatus(u[17]);
            newUsersList.add(usr);
        }

        List<User> res[] = UserManager.compareUsers(usersListInDB, newUsersList);
        writer.println("Updated Users:" + res[0].size());
        writer.println("Inserted Users:" + res[1].size());
        writer.flush();
        writer.close();
    }
}
